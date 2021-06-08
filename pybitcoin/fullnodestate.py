from enum import Enum


class FullNodeState(str, Enum):
    Created = 'Created'
    Initializing = 'Initializing'
    Initialized = 'Initialized'
    Starting = 'Starting'
    Started = 'Started'
    Disposing = 'Disposing'
    Disposed = 'Disposed'
    Failed = 'Failed'
