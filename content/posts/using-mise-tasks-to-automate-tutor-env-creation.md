---
title: "Using Mise Tasks to Automate Tutor Env Creation"
subtitle: ""
date: 2026-01-19T12:16:45+11:00
lastmod: 2026-01-19T12:16:45+11:00
draft: false
author: ""
authorLink: ""
description: ""
license: ""
images: []

tags:
  - openedx
  - mise
  - tutor
categories:
  - Coding
---

I have [previously written about using Mise]({{< ref "managing-open-edx-tutor-with-mise" >}}) to manage multiple versions of Open edX Tutor. It had it's limitations and involved using a custom library I created to handle versions. I soon grew out of it. Since Tutor plugins are Python packages, it's best to create dedicated virtual environments to keep things separate and self contained.
<!--more-->

So, [the solution we came up with at OpenCraft](https://forum.opencraft.com/t/new-recommendations-for-devstacks/1845) was to designate a directory as a Tutor environment, create a Python virtual environment inside it and let Mise handle all the paths. That takes care of managing multiple versions in isolated environments.

### Automating the setup

Using mise's tasks, the setup can be automated using a shell script.

```sh
#!/usr/bin/env bash
#MISE dir="{{cwd}}"

# Script to automatically setup a Tutor Environment based on the release name

set -euo pipefail

RELEASE="${1:-main}"

cd $PWD
mkdir -p plugins
mise use python@3.12
mise config set env._.python.venv.path ".venv"
mise set TUTOR_ROOT="$PWD"
mise set TUTOR_PLUGINS_ROOT="$PWD/plugins"

echo "Creating a virtual environment"
python -m venv .venv
source .venv/bin/activate
echo "Installing Tutor in the virtualenv at .venv for release: $RELEASE"

case "$RELEASE" in
  "ulmo")
    echo "Running: pip install 'tutor[full]>=21.0.0,<22.0.0'"
    pip install 'tutor[full]>=21.0.0,<22.0.0'
    ;;
  "teak")
    echo "Running: pip install 'tutor[full]>=20.0.0,<21.0.0'"
    pip install 'tutor[full]>=20.0.0,<21.0.0'
    ;;
  "sumac")
    echo "Running: pip install 'tutor[full]>=19.0.0,<20.0.0'"
    pip install 'tutor[full]>=19.0.0,<20.0.0'
    ;;
  "redwood")
    echo "Running: pip install 'tutor[full]>=18.0.0,<19.0.0'"
    pip install 'tutor[full]>=18.0.0,<19.0.0'
    ;;
  "main")
    echo "Cloning tutor main branch from Github"
    git clone --branch=main https://github.com/overhangio/tutor.git
    pip install -e "./tutor[full]"
    ;;
  *)
    echo "Unknown release: $RELEASE" >&2
    exit 1
    ;;
esac
```

### How to use?

Put this script in `~/.config/mise/tasks/tutor-env.sh` make it executable with `chmod +x tutor-env.sh`.

* New environments can be created with a simple `mise run tutor-env <openedx-release>`. It will install the appropriate Tutor version for the Open edX release. 
* If no `<openedx-release>` is passed, it will clone setup `tutor-main`. 
* This will also create a `plugins` directory and set it as the `TUTOR_PLUGIN_ROOT`.

I find it super helpful as I keep losing track of the Tutor version that corresponds the an Open edX release.
