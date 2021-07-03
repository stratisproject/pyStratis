from enum import Enum


class FullNodeState(str, Enum):
    """Enum representing current state of Full Node."""
    Created = 'Created'
    Initializing = 'Initializing'
    Initialized = 'Initialized'
    Starting = 'Starting'
    Started = 'Started'
    Disposing = 'Disposing'
    Disposed = 'Disposed'
    Failed = 'Failed'
