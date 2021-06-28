# drowsy-detector
Driver drowsiness dectection system, SnT Project computer Vision.
## Installing and Configuring dlib:
We need to create an enivronment in order to install dlib, Since trying to install it directly using pip command is not possible as it is C++ lib. So, follow this commands in order to install dlib into your system if you haven't installed it previously. We are using Anaconda for installing it. 
### Step 1: Update conda 
```bash
conda update conda
```
### Step 2: Update anaconda 
```bash
conda update anaconda 
```
### Step 3: Create a virtual environment
```bash 
conda create -n env_dlib 
```
### Step 4: Activate the virtual environment 
```bash 
conda activate env_dlib
```
### Step 5: Install dlib 
```bash 
conda install -c conda-forge dlib 
```
If all these steps are completed successfully, then dlib will be installed in the virtual environment <b>env_dlib</b>. Make sure to use this environment to run the entire project. 

### Step to deactivate the virtual environment 
```bash 
conda deactivate 
```

## Running the system: 

### Clone and run: 
Clone the repository into your system by: 
```bash 
git clone https://github.com/fear-the-lord/Drowsiness-Detection.git
```
Press ESC to exit from running program.
