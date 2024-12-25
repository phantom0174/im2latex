## Training

Follows the same procedure from [original readme](./README-ori.md)

## Generalization testing

0. Put model at `./test_model/`, set `USE_OUR_CNN` to true if model name has suffix `new`, and change args in `real_world.py` (line 21)

1. Put real-world images at `./real/imgs/`

2. Preprocess data: `python preprocess_real.py`, can set different images resized height with changing `new_height` variable. 

3. Start prediction: `python real_world.py`

4. Result is stored at `./real_results/`
