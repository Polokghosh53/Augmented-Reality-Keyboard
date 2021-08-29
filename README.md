# Augmented-Reality-Keyboard
In this project, a virtual keyboard is created which is operated by pointing a key on a virtual grid using camera. First a grid is keyboard grid is made. A random is chosen and made into a physical pointer. This is obtained by thresholding. Every time the pointer stays above a key for a given interval, the key is clicked and the input is saved.

PyCharm is used here for efficient programming.

## Dependencies
`pip install -r requirements.txt`

## Process
* Use `https://github.com/Polokghosh53/Augmented-Reality-Keyboard.git` to clone the files in your local directory.
* Install the dependencies in PyCharm IDE using the terminal console or command prompt.
* Go to `Run`>`Edit Configurations` after selecting or clicking the `range_det.py` file. After a window opens write `--filter HSV --webcam` on `Parameters` and click Apply. This activates the threshold bar window to open up and do the manual adjustment to the color pointer.
![python pic](https://user-images.githubusercontent.com/57084217/131241749-4b1ac918-1263-4557-96cf-1dd4558bb21c.PNG)

* Then, run the `range_det.py` file and adjust the color pointer and then the value will be saved in a `range.pickle` file for the color pointer to work on the main file.
* Now, run the `AR-Keyboard.py`.

**NOTE**: Works on single finger input during the keyboard input.

## Achievements
![SESSION21](https://user-images.githubusercontent.com/57084217/131241956-cc982633-bdf2-4727-9404-15a2a5c90e51.jpg)
![python pic](https://user-images.githubusercontent.com/57084217/131242014-048eeb45-b01e-4957-b8aa-0b6bb234ebb6.PNG)
