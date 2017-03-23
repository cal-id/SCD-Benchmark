# Benchmarking
## Builds
### Cloud

* **build.sh** - the build script to install IMB and HPL

* **Make.Linux_SL6_Intel64** - a makefile required to be copied in before building HPL

* **setupSSH.sh** - a script to setup SSH between hosts (requires editing to insert hostname of the other host)

### JASMIN_SCARF

* **buildIMB.sh** - a script to install IMB on JASMIN and SCARF

### Location of HPL
* LOTUS: `/apps/src/hpl/hpl-2.2/bin/Linux_Intel64/xhpl`
* SCARF: `/apps/procspec/hpl/2.2/bin/Linux_Intel64/xhpl`

## Tests
### Completed
| Infrastructure | HPL | IMB |
| -------------- | --- | --- |
| SCARF          | yes | yes |
| JASMIN         | no  | yes |
| Cloud          | no  | yes |

### Useful scripts
* **parseHostGroups/parseByHostgroup.py** - a script to create a json file mapping hosts to hostgroups for LSF (SCARF and JASMIN)
* **makeClean.sh** - a script to remove .err files from `outputs/` (a subdirectory of where it is run from)

### HPL configuration
Under `Configure_HPL/HPL.dat` is the configuration file used for all HPL tests.

## Results

### Results for
#### IMB
* SCARF
* Cloud

### To Do Analysis
### To Get Results
#### IMB
* JASMIN

#### HPL
* SCARF
* JASMIN
* Cloud
