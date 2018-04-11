# Network Based Inference

This project containbs code implementing the Network Based Inference technique for use as a recommendation engine. 

## Getting Started

The code implemented works as a sci-kit learn classifier. It will fit the NBI weighted adjacency matrix on a bipartite graph of
person-by-object. It will then predict likely objects for a new person, given any past object acquisition behaviour. Please see the reference 
below for the details of algorithm.

### Prerequisites

The following packages will be needed to run the code.

```
sklearn
numpy
```

## Authors and References

* Iain J. Cruickshank
* Tao Zhou, Jie Ren, Matus Medo, and Yi-Cheng Zhang, Bipartite network projection and personal recommendation. Physical Review E 76(4): 046115, 2007

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

