# This is an exemplary script file for testing purposes using pytest.
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def test_plot_sine_wave(save_folder):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.show()
    plt.savefig(save_folder + '/sin_plot.png')
    
    # Test if y is really a sine wave
    assert np.allclose(y, np.sin(x))
    
    # Test if the save_folder is a string
    assert isinstance(save_folder, str)
    
    # Test if the save_folder is not empty
    assert save_folder != ''
    
    
