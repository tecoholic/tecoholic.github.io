---
title: "Creating Opticks Plug-in From Scratch"
slug: "creating-opticks-extension-from-scratch"
categories:
  - Notes
tags:
  - opticks
  - dev-notes
  - windows
---

> Windows Only

### Rant about bad documentation in Opticks

I was to build a custom Plug-in for the open source satellite image processing software [Opticks](http://www.opticks.org) in the college. Extension, plugin, addon - anyway you call it. It has always been my playground. So I thought this would be another quick dip in a new pool. I was wrong. They have a seperate Plug-in development SDK and all their problems start there. You can run through their documentation umpteen times, all times you would end up is a place that has a set of instructions telling you to build the sample plugins and the Plug-in development tutorials using a previously setup Microsoft Visual Studio project and a batch file called retrive_dependencies.bat running a Java jar file. What is bad about it? Because I donot know what the damn settings I have to set in the project settings, what are my dependencies and no clue how to create a plugin other than the sample plugins. YES. NO CLUE TO CREATE NEW Plug-in FROM SCRATCH.

My previous endeavors with Mozilla's Firefox Addon SDK, QuantumGIS's new plugin scripts have all gone well. I did not expect something similar, because I knew I am building for a Windows application, where terminals and scripts are almost non-existant. But lack of even a HowTo in setting up the project workspace was too much of a let down.

### So how to do it actually?

* Download the Opticks Plug-in Development SDK
* Extract the SDK zip into a convenient location. Selecting a folder in root of a drive will be a good choice.
* Open Visual Studio or Express which you have installed.
* Create a "New Project"
* Select the project type to be "Win32 Console Application" from "Visual C++"
* Give a name and select a project location 
* In the "Win32 Application Wizard" that opens, Click `Next` and select `DLL` for "Application Type" and select `Empty Project` in "Additional Options"
* Now Click `Finish` and create the project
* A Opticks plugin basically needs 3 files: ModuleManager.cpp, PluginName.h, PluginName.cpp. The ModuleManger.cpp registers the namespace for your plugin with Opticks, the PluginName.h and the Plugin.cpp contains the plugin funtionality. You may include mutiple PluginName kind of header and cpp files if your plugin is to perform multiple funtions. Read more [here](http://opticks.org/docs/sdk/4.7.1/register_plugin.html) about the ModuleManager file (Also see Note at the bottom). And about what to put in your plugin files in [Tutorial1](http://opticks.org/docs/sdk/latest-stable/plugintutorial1.html)
* For the purpose of illustrating I copied the files ModuleManager.cpp, Tutorial1.h and Tutorial2.h from `SDK_HOME/application/PlugIns/src/Tutorial` to my project directory
* Now in Visual Studio/Express, right-click the project in "Solution Explorer", `Add` -> `Existing Item` -> select the files we copied into our project and save the project
* In the menu, `Build` -> `Configuration Manager` set "Active Solution configuration" to "Release" and close. (Plugins compiled in Debug mode crashes the application while starting. I think the whole application has to be cutom compiled in debug mode for them to be compatible)
* Right-click on the project again and select `Properties`
* In the `Configuration Properties`, select `C/C++`. Edit "Additional Include Directories" to include the following directories

```
SDK_HOME/application/PlugInUtilities/Interfaces
SDK_HOME/application/PlugInManager
SDK_HOME/application/PlugInLib
SDK_HOME/application/Interfaces
```

* In the `Linker`, edit "Additional Library Directories" to include `SDK_HOME/Build/Binaries-Win32-release/Lib` or x64 if that is your platform. Click `Ok` and close the Properties. Ideally this should include the .lib files while linking, but this doesn't seem to work. So do the next step.
* Right-click the project in `Solution Explorer` again, select `Add` -> `Existing Item` and select the libraries `PluginLib.lib` `PlugInUtilities.lib` `SimpleApiLib.lib` (You may want to include other libs later, but for now this will do)
* Hit Build
* Now collect your dll file from the `Release` dir of your project and put it in `<Install Location>/Opticks/<version>/PlugIns/`
* Start Opticks and you can find a item called Tutorial Menu in the plugin toolbar or you can Right-click somewhere on the toolbar and enable it.
* Finally thank me for the post :)

__Note:__ The documentation about the Registering Plugin modules has a small mistake. The documentation in this page -> http://opticks.org/docs/sdk/4.7.1/register_plugin.html states there are two macros to register the plugin:

* REGISTER_PLUGIN which takes **two** arguments for a constructor without arguments and
* REGISTER_PLUGIN_BASIC which takes **three** arguments for a constructor with three arguments

I assume there was a typo there it is actually **REGISTER_PLUGIN** which takes **three** arguments and **REGISTER_PLUGIN_BASIC** which takes **two** arguments.

