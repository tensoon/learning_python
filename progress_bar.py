import time
import progressbar

bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
for i in range(201):
    time.sleep(0.1)
    bar.update(i)
