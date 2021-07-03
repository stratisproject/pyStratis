from enum import Enum


class FeatureInitializationState(str, Enum):
    """Enum representing current state of feature initialization."""
    Uninitialized = 'Uninitialized'
    Initializing = 'Initializing'
    Initialized = 'Initialized'
    Disposing = 'Disposing'
    Disposed = 'Disposed'
