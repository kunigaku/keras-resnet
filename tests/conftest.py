import keras.layers
import pytest


@pytest.fixture(scope="module")
def x():
    shape = (224, 224, 3)

    return keras.layers.Input(shape)


@pytest.fixture(scope="module")
def x1d():
    shape = (310, 2)

    return keras.layers.Input(shape)
