---
layout: post
title: "Simplifying a Factory Pattern function that has grown complex"
date: 2020-04-06 07:29:05
category: Coding
tags: python software
---

> This is a combination of the problem that I posted in [Dev.to](https://dev.to/tecoholic/what-is-the-right-design-pattern-to-employ-fk6) and [StackExchange](https://softwareengineering.stackexchange.com/questions/408401/how-to-simplify-a-complex-factory-pattern) and the final solution that I adopted.


### The Problem



I have a function which takes the incoming request, parses the data and performs an action and posts the results to a webhook. This is running as background as a Celery Task. This function is a common interface for about a dozen Processors, so can be said to follow the Factory Pattern. Here is the psuedo code:

```python
processors = {
 "action_1": ProcessorClass1, 
 "action_2": ProcessorClass2,
 ...
}

def run_task(action, input_file, *args, **kwargs):
 # Get the input file from a URL
 log = create_logitem()
 try:
 file = get_input_file(input_file)
 except:
 log.status = "Failure"

 # process the input file
 try:
 processor = processors[action](file)
 results = processor.execute()
 except:
 log.status = "Failure"

 # upload the results to another location
 try:
 upload_result_file(results.file)
 except:
 log.status = "Failure"

 # Post the log about the entire process to a webhoook
 post_results_to_webhook(log)
```

This has been working well for most part as the the inputs were restricted to action and a single argument (`input_file`). As the software has grown, the processors have increased and the input arguments have started to vary. All the new arguments are passed as keyword arguments and the logic has become more like this.

```python
try:
 input_file = get_input_file(input_file)
 if action == "action_2":
 input_file_2 = get_input_file(kwargs.get("input_file_2"))
except:
 log.status = "failure"


try:
 processor = processors[action](file)
 if action == "action_1":
 extra_argument = kwargs.get("extra_argument")
 results = processor.execute(extra_argument)
 elif action == "action_2":
 extra_1 = kwargs.get("extra_1")
 extra_2 = kwargs.get("extra_2")
 results = processor.execute(input_file_2, extra_1, extra_2)
 else:
 results = processor.execute()
except:
 log.status = "Failure"
```

Adding the if conditions for a couple of things didn't make a difference, but now almost 6 of the 11 processors have extra inputs specific to them and the code is starting to look complex and I am not sure how to simplify it. Or if at all I should attempt at simplifying it.

Something I have considered:
1. **Create a separate task for the processors with extra inputs** - But this would mean, I will be repeating the file fetching, logging, result upload and webhook code in each task.
2. **Moving the file download and argument parsing into the BaseProcessor** - This is not possible as the processor is used in other contexts without the file download and webhooks as well.

The solution
------------



I solved it by making two important changes:

1. Normalised the processor's by making the common arguments positional and everything else keyword based. This allows me to pass the `kwargs` as I receive them without unpacking. It is the processor's job.
2. For the extra files, make a copy of the kwargs and replace the remote file url with the local file location. This way, the extra files are a part of the kwargs dict itself.



```python
def run_task(action, input_file, *args, **kwargs):

 params = kwargs.copy()

 # Get the input file from a URL
 log = create_logitem()
 try:
 file = get_input_file(input_file)
 if action == "action_2":
 params["extra_file"] = get_input_file(kwargs["extra_file"] # update the files in params
 except:
 log.status = "Failure"

 # process the input file
 try:
 processor = processors[action](file)
 results = processor.execute(**params) # Unpack and pass the params
 except:
 log.status = "Failure"

 # upload the results to another location
 try:
 upload_result_file(results.file)
 except:
 log.status = "Failure"

 # Post the log about the entire process to a webhoook
 post_results_to_webhook(log)
```

Now I have the same lean structure as I originally had. The only processor specific code is the file downloads which I think I can live with for now.

### Credits


[Kain0_0](https://softwareengineering.stackexchange.com/users/319783/kain0-0)'s answer pointed me in the right direction and helped me simplify it in a way that makes sense.
