from enum import Enum


class FeatureInitializationState(str, Enum):
    Uninitialized = 'Uninitialized'
    Initializing = 'Initialized'
    Initialized = 'Initialized'
    Disposing = 'Disposing'
    Disposed = 'Disposed'
