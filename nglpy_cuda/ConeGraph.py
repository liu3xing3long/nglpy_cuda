"""
    The API for using NGLPy with CUDA
"""
import nglpy_cuda as ngl
from .Graph import Graph


class ConeGraph(Graph):
    """ A neighborhood graph that represents the connectivity of a given
    data matrix.

    Attributes:
        None
    """

    def __init__(self,
                 index=None,
                 max_neighbors=-1,
                 num_sectors=6,
                 points_per_sector=1,
                 algorithm="yao",
                 query_size=None,
                 cached=True):
        """Initialization of the graph object. This will convert all of
        the passed in parameters into parameters the C++ implementation
        of NGL can understand and then issue an external call to that
        library.

        Args:
            index (string): A nearest neighbor index structure which can
                be queried and pruned
            max_neighbors (int): The maximum number of neighbors to
                associate with any single point in the dataset.
            num_sectors (int): The number of roughly equal sized conic
                sectors that the space around the point should be split
            points_per_sector (int): The maximum number of nearest
                neighbors to keep per sector
            algorithm (str): a string representation of the type of
                graph to compute should be yao or theta
            query_size (int): The number of points to process with each
                call to the GPU, this should be computed based on
                available resources
            cached (bool): Flag denoting whether the resulting computation
                should be stored for future use, will consume more memory,
                but can drastically reduce the runtime for subsequent
                iterations through the data.
        """
        super(ConeGraph, self).__init__(
            index=index,
            max_neighbors=max_neighbors,
            query_size=query_size,
            cached=cached
        )

        self.num_sectors = num_sectors
        self.points_per_sector = points_per_sector
        self.algorithm = algorithm

    def compute_query_size(self):
        """
        """
        if self.query_size is not None:
            return self.query_size
        return self.query_size

    def collect_additional_indices(self, edges, indices):
        return indices

    def prune(self, X, edges, indices=None, count=None):
        return edges