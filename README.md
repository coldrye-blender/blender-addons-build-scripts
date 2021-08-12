# blender-addons-build-scripts

This is meant to be used as a submodule in git from where the provided scripts can be executed from during
the build process.


## Example Usage

```shell
> git submodule add https://github.com/coldrye-solutions/blender-addons-build-scripts.git scripts
```


## Platform Specific Information


### Linux

Just install Python3, PIP3 and you are good to go.


### MacOS

Since I do not have access to MacOS right now, you will have to figure out things by yourself.


### Windows 10+ (Frickin' Special Cases)

You need to have [Git for Windows](https://gitforwindows.org/) installed in order to run the scripts located in bin.

In addition, you will have to disable the aliases for Python2 and Python3 in your Windows apps settings
(Settings -> Apps -> Aliases ...) in order to make this work.

Next, install a version of Python3 that is compatible with the target Blender release version.

Inside Git for Windows / Git Bash, you need to add a path to the location where the so installed Python version
lives, e.g.

```shell
> export PATH=$PATH:/c/.../Python3.x.x/
```

And you will also have to install PIP3.

From now on, you can use Git Bash to execute any of the scripts inside the bin folder, e.g.

```shell
> ./bin/meta show --help
```


#### Thank You, No Extra Brainfuck Needed

No. We will not add any "Power"Shell CMDLETs or BATCH scripts to this repo. Have you ever looked at the syntax of
these scripts? Brainfuck, unmaintainable, not portable and overly complex, they are. Therefore, we will have no such
shenanigans. Let them deal with their junk syntax and overly complex systems, since we will not add yet another special
case to this repository except for the information presented in the section above.

And, given the current state of the scripts, they will work just fine with any platform that runs (git)bash.
In fact, these scripts have been developed under Windows 10 / GitBash and will work just as well under Linux or MacOs.


## Install Requirements

Once you have installed Python3 and PIP3, you will have to install the requirements from the `requirements.txt` file.
And if you are using a virtual env, which you should, make sure to activate it first prior to installing the
requirements.

```shell
> pip3 install -r requirements.txt
```
