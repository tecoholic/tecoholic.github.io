---
title: "Replacing image in a PDF with Python"
date: 2019-01-29T10:38:34
slug: "replacing-image-in-a-pdf-with-python"
categories:
  - Coding
tags:
  - python
---

Being a freelancer is an interesting role. You come across a variety of projects. I recently worked on a project involving replacing images in a PDF which taught me a couple of things.

1. While there are a number of tools to deal with PDF in Python, the general purpose tools can only do so much because... reason 2
2. PDF is a dump of instructions to put things in specific places. There is no logical way it is done that make general purposes tools manipulate the PDF in a consistent way.
3. Not everything is bad. Almost all positive changes like adding text or image and whole page changes like rotating, cropping are usually possible and so are all read operations like text, image extraction ..etc.,
4. The issue is when you want to delete something and replace it with something else.



With that learnt, I set out to achieve the goal anyway.

### Step 1 - Understanding the format



Humans invented the PDF format, which means they used words to describe things in the file, which means we can read them. So opening a PDF file in a text editor like VIM will show something like this.

![PDF in VIM](/img/wp-content/uploads/2019/01/screenshot-2019-01-28-at-9.58.10-pm.png)

Without getting into the entirety of the PDF spec, let us see what this means. PDF is a collection of objects. There is usually an identifier like `int int obj` followed by some metadata and then a stream of binary information starting with `stream` and ends with `endstream` and `endobj`. A image in our case would be represented as

```text
16 0 obj
<< /Length 17 0 R /Type /XObject /Subtype /Image /Width 242 /Height 291 /Interpolate
true /ColorSpace 7 0 R /Intent /Perceptual /BitsPerComponent 8 /Filter /DCTDecode
>>
stream
Image binary data here like ÿØÿá^@VExif^@^@MM^@*^@^@^@^H^@^D^A^Z^@^E^@^@
endstream
endobj
```

So to successfully replace an image we will have to replace the image binary data and the metadata like width and height.

### Step 2 - Uncompressing the PDF and extracting the images



Use a PDF manipulation called toolkit called PDFtk.

```text
pdftk sample.pdf output uncompressed.pdf uncompress
```

What this command does is, it uncompresses the file and makes it easier to read and manipulate. Let us open the `uncompressed.pdf` in VIM to see the difference.

![uncompressed pdf](/img/wp-content/uploads/2019/01/uncompressed-pdf.png)
### Step 3 - Identifying the image to replace



PDF is essentially a collection of objects and a PDF file might contain multiple images, there is no way to identify a particular image in the binary data of the PDF file (unless you are from Matrix). We will have to first extract the images from the PDF and match the PDF object to the image using its metadata like height and width. To do that install `pdfimages` command-line tool (part of poppler-utils) and run `pdfimages -list uncompressed.pdf`. This will list all the images in the PDF with their metadata.

```text
page num type width height color comp bpc enc interp object ID x-ppi y-ppi size ratio
--------------------------------------------------------------------------------------------
 1 0 image 277 185 icc 3 8 jpeg yes 11 0 113 113 69.2K 46%
 1 1 image 277 185 icc 3 8 jpeg yes 10 0 113 113 31.9K 21%
 1 2 image 242 291 icc 3 8 jpeg yes 12 0 112 112 55.2K 27%
```

Next extract all the images in their original formats using

```bash
pdfimages -all uncompressed.pdf image
```

That extracts the files and names them after the prefix we provided like this `image-000.jpg image-001.jpg image-002.jpg`.

Now open your images check their file's height, width and file size and mark the details for the one to replace. In my case the file details were:

* height - 185
* width - 277
* size - 70836



There are two images which matches the height and width, thankfully they have different file sizes.

### Step 4 - Identifying the object in PDF that represents the image



I opened the `uncompressed.pdf` in VIM and searched for the most unique value I have found for the image - its size.

![identifying the image object](/img/wp-content/uploads/2019/01/identifying-the-image-object.png)

Now we can identify the object identifier, in this case it is `11 0 obj`.

### Step 5 - Replacing the image with another image



Now the job is to switch the object 11's image data with our image's data. You can use the following Python script to achieve that.

https://gist.github.com/e44f727f77c74e50f4d70ff10539350b

Download the file, change the `OBJECT_ID` value, save the file and run:

```text
python process.py <your pdf> <new image>
```

I just used the one of the extracted images to replace another one. So here are the before and after images.

![image replaced pdf](/img/wp-content/uploads/2019/01/image-replaced-pdf.png)
### Step 6 - Compressing the file back (OPTIONAL)



Do this only if you really need to do it for some reason. It is usually cool to just use the uncompressed file.

```text
pdftk uncompressed.pdf output replaced.pdf compress
```
