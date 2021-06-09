from enum import Enum


class FeatureInitializationState(str, Enum):
    Uninitialized = 'Uninitialized'
    Initializing = 'Initializing'
    Initialized = 'Initialized'
    Disposing = 'Disposing'
    Disposed = 'Disposed'
