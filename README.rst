Ref
~~~

:API doc: `<https://docs.ceph.com/en/latest/api/>`_
:bluestore: OSD - data is written directly to the disk device, while a separate
    RocksDB key-value store contains all the metadata. BlueFS provides a
    virtual filesystem layer to support RocksDB.
..  layout: block, block.db, block.wal
:build:  `<https://docs.ceph.com/en/latest/install/build-ceph/>`_
         `<https://docs.ceph.com/en/latest/dev/quick_guide/>`_
         `<https://docs.ceph.com/en/latest/dev/macos/>`_
:cbt:  Ceph Benchmarking Tool - `<https://github.com/ceph/cbt>`_
       `<https://www.youtube.com/watch?v=yZX1oNqrJMk>`_
       
..  slow requests 30secs
..  gstack, gcore
:cephadm:  Ceph orchestrator - `/ceph/src/cephadm`
           `<https://ceph.io/en/news/blog/2025/automating-ceph-cluster-deployments_part1/>`_

    cephadm deploys all Ceph daemons as containers using Docker or Podman.
:cephFS:  `<https://www.kernel.org/doc/html/latest/filesystems/ceph.html>`_

    `</linux/include/linux/ceph/>`_
    `</linux/drivers/fs/ceph/>`_
:ci:     `<https://github.com/ceph/teuthology>`_

:cli:

    `</ceph/src/ceph.in>`_

:cluster map:

    `<https://docs.ceph.com/en/latest/architecture/#cluster-map>`_

:compiler:

    `</ceph/src/crush/CrushCompiler.h>`_  FIXME
:contrib:  `<https://docs.ceph.com/en/latest/dev/developer_guide/basic-workflow/#basic-workflow-dev-guide>`_
           `<https://docs.ceph.com/en/latest/start/documenting-ceph/#documenting-ceph>`_

:crush:  `</ceph/src/crush/mapper.h>`_
         `<https://ceph.io/assets/pdfs/weil-crush-sc06.pdf>`_

    `</ceph/src/crush/mapper::crush_do_rule>`_ - RADOS, OSD
    `</linux/net/ceph/crush/mapper::crush_do_rule>`_ - CephFs, RBD

..  "CRUSH is implemented as a pseudo-random, deterministic function that maps
    an input value, typically an object or object group identifier, to a list
    of devices on which to store object replicas."

..  "CRUSH meets these challenges by casting data placement as a pseudo-random
    mapping function, eliminating the conventional need for allocation metadata
    and instead distributing data based on a weighted hierarchy describing
    available storage."

..  Weight sets allow the cluster to perform numerical optimization based on the
    specifics of your cluster (for example: hierarchy, pools) to achieve a balanced
    distribution.

    ref `<https://docs.ceph.com/en/latest/rados/operations/crush-map/#weight-sets>`_

..  workload vs utilisation

    "Although a large system will likely contain devices with a variety of
    capacity and performance characteristics, randomized data distributions
    statistically correlate device utilization with workload, such that device
    load is on average proportional to the amount of data stored. This results
    in a one-dimensional placement metric, weight, which should be derived from
    the device's capabilities. Bucket weights are defined as the sum of the
    weights of the items they contain."

..  reshuffling

    "In contrast to conventional hashing techniques, in which any change in the
    number of target bins (devices) results in a massive reshuffling of bin
    contents, CRUSH is based on four different bucket types, each with a
    different selection algorithm to address data movement resulting from the
    addition or removal of devices and overall computational complexity."

..  CSP

    "The data distribution policy is defined in terms of placement rules that
    specify how many replica targets are chosen from the cluster and what
    restrictions are imposed on replica placement. For example, one might
    specify that three mirrored replicas are to be placed on devices in
    different physical cabinets so that they do not share the same electrical
    circuit."

    table 1 defines a placement rule, algorithm 1 the placement algorithm;
    a scripting language over the tree traversal of the cluster map

    "Generally speaking, CRUSH is designed to reconcile two competing goals:
    efficiency and scalability of the mapping algorithm, and minimal data
    migration to restore a balanced distribution when the cluster changes
    due to the addition or removal of devices."
    
..  weights (sec 3.3),

    m_optimal = Dw/W where 
    Dw is the combined weight of the storage devices added or removed, and
    W is the total weight of the system.

..  buckets: uniform, list, tree, straw

..  overload protection (sec 4.1.1)

..  load balancing (sec 4.1.2)

..  hashing function (sec 4.3, 5)

..  quantified overall system reliability, MTTDL (sec 4.4, 5)

..  tree size n^CRUSH_MAX_DEPTH == n^10?

..
    `</ceph/src/crush/mapper::crush_ln>`_
    RH Reciprocal High
    LH Logarithmic High
    LL Logarithmic Low

..
    User space wrapped under `<src/crush/CrushWrapper::do_rule>`

    FIXME: algorithm
..
    `</Users/dion/Documents/gitspace/ceph/doc/rados/operations/crush-map.rst>`_

    The CRUSH map consists of (1) a hierarchy that describes the physical topology
    of the cluster and (2) a set of rules that defines data placement policy. The
    hierarchy has devices (OSDs) at the leaves and internal nodes corresponding
    to other physical features or groupings: hosts, racks, rows, data centers,
    and so on. [...] "Bucket", in the context of CRUSH, is a term for any of the
    internal nodes in the hierarchy.

    ref `<https://docs.ceph.com/en/latest/rados/operations/crush-map/#crush-structure>`_
    ref `</ceph/src/osd/OSDMap::_build_crush_types>`_

:crush map:  `<https://docs.ceph.com/en/latest/rados/operations/crush-map-edits/>`_

    `</ceph/src/crush/crush::crush_map>`_
    `</linux/include/linux/crush/crush::crush_map>`_

..  /ceph/src/crush/crush::crush_get_bucket_item_weight  FIXME what is?
..  /ceph/src/crush/builder::set_optimal_crush_map  **creation**
..  /ceph/src/crush/builder::crush_bucket_add_item  **reallocs**
....  bucket size unbounded?
....  rule size unbounded?
..  /ceph/src/crush/mapper::crush_do_rule
....  recursive calls

:erasure code:  `<https://docs.ceph.com/en/latest/rados/operations/crush-map/#creating-a-rule-for-an-erasure-coded-pool>`_

..  erasure coding enhancements `</ceph/doc/dev/osd_internals/erasure_coding/enhancements.rst>`_
:fsid:

    The fsid is a unique identifier for the cluster, and stands for
    File System ID from the days when the Ceph Storage Cluster was principally
    for the Ceph File System.

    `<https://docs.ceph.com/en/latest/install/manual-deployment/#monitor-bootstrapping>`_
:glossary:  `<https://docs.ceph.com/en/latest/glossary/>`_

:hello:

    `</ceph/src/pybind/mgr/hello/module.py>`_
:ibm:  `<https://www.ibm.com/docs/en/storage-ceph>`_
       `<https://www.redbooks.ibm.com/abstracts/redp5721.html>`_

:init:
    `</ceph/src/mon/MonClient::MonClient::init>`_

:ioctl:  `</linux/fs/ceph/ioctl::ceph_ioctl>`_

:jerasure:
    `<src/erasure-code/jerasure/jerasure/README>`_

..  FIXME: ceph plugins?

:main:

    OSD - `</ceph/src/ceph_osd::main>`_
    MDS - `</ceph/src/ceph_mds::main>`_
    MGR - `</ceph/src/ceph_mgr::main>`_
    MON - `</ceph/src/ceph_mon::main>`_
    RGW (S3) - ?

..  Ceph Monitors maintain the master copy of the cluster map, which they
    provide to Ceph clients. The existence of multiple monitors in the Ceph
    cluster ensures availability if one of the monitor daemons or its host
    fails.

    A Ceph OSD Daemon checks its own state and the state of other OSDs and
    reports back to monitors.

    A Ceph Manager serves as an endpoint for monitoring, orchestration, and
    plug-in modules.

    A Ceph Metadata Server (MDS) manages file metadata when CephFS is used to
    provide file services.

    see `<https://docs.ceph.com/en/latest/architecture/>`_
:MSR (Multi-step Retry):  `</ceph/doc/dev/crush-msr.rst>`_
:paxos,raft:  `<https://raft.github.io/raft.pdf>`_
    `</ceph/src/mon/Paxos.h>`_

..  One or more instances of ceph-mon form a Paxos part-time parliament
    cluster that provides extremely reliable and durable storage of cluster
    membership, configuration, and state.
    see `</ceph/debian/control>`_

:pybind:

    Py API: `<https://docs.python.org/3/extending/index.html>`_
    ex `</ceph/src/mgr/ActivePyModule.cc>`_

    GIL: `</ceph/src/mgr/Gil.h>`_
:rados:  `/ceph/src/librados`
         `<https://ceph.io/assets/pdfs/weil-rados-pdsw07.pdf>`_
         `<https://docs.ceph.com/en/latest/rados/api/>`_

..  Each object is mapped into a placement group (PG).
    Placement groups are assigned to OSDs, CRUSH does the mapping.
..  librados `<https://docs.ceph.com/en/latest/rados/api/librados-intro/>`_
:rados bench: `</ceph/src/tools/rbd/action/Bench.cc>`_, registered through `<Shell::get_actions>`_
:rados block device: RBD

:RBD: RADOS block device
:S3 lifetime management: tiering system
:subsystems:  `<https://docs.ceph.com/en/latest/rados/troubleshooting/log-and-debug/#ceph-subsystems>`_
:test:  `<https://docs.ceph.com/en/latest/dev/developer_guide/tests-unit-tests/>`_

    `</ceph/src/test/crush/CMakeLists.txt>`_

:vstart: `<https://docs.ceph.com/en/latest/dev/dev_cluster_deployment/#dev-deploying-a-development-cluster>`_
         `<https://docs.ceph.com/en/latest/dev/quick_guide/>`_

..  logs `build/out`
         
..  FIXME MGR::balancer?
..  FIXME MGR::auto-scaler?
..  FIXME MGR::prometheus?
    
:www:  `<https://docs.ceph.com/en/latest/start/get-involved/>`_

Contrib
~~~~~~~

:conf: `./build/ceph.conf`
:coredump:  FIXME
:crush map:

    ceph osd getcrushmap -o {compiled-crushmap-filename}
    crushtool -d {compiled-crushmap-filename} -o {decompiled-crushmap-filename}

    ceph osd crush dump  #  json of the crush map

:gdb:
    gdb --batch -ex "source ../extensions/pygdb.py" -p `cat ./out/mon.a.pid`
:intro:
    export DOCKER_DEFAULT_PLATFORM=linux/amd64
    docker run -it --stop-signal SIGQUIT --privileged --cap-add=SYS_PTRACE --security-opt seccomp=unconfined  --name ceph -v ~/Documents/gitspace:/mnt/macos --net=host  debian:testing
    ./install-deps.sh
    git submodule deinit --force --all
    git submodule update --init --recursive --progress --recommend-shallow  --jobs 11
    ./do_cmake.sh -DWITH_MANPAGE=OFF -DWITH_BABELTRACE=OFF -DWITH_MGR_DASHBOARD_FRONTEND=OFF -DWITH_RBD=OFF -DWITH_KRBD=OFF -DWITH_RADOSGW=OFF -DWITH_TESTS=OFF -DWITH_SYSTEM_BOOST=ON  (cmake -LH)
    ./run-make-check.sh
    cd build; ninja -t targets all
    env MON=1 MDS=1 OSD=1 ../src/vstart.sh --new -x --localhost --bluestore  --debug --trace
                          ../src/stop.sh
:ctest:
    ninja -t targets all (check,test)
    ninja unittest_crush && ./bin/unittest_crush --gtest_filter="CRUSHTest.indep_basic"  (--gtest_list_tests)

:ceph --cluster {cluster-name}:
:ceph health detail:
:ceph mgr services:
:ceph osd pool stats:
:ceph osd pool create mypool:
:ceph osd tree:

:ceph osd crush rule ls:  `<https://docs.ceph.com/en/latest/rados/operations/crush-map/#rules>`_
:ceph osd crush rule dump:

:rados df:
:rados -p mypool bench 10 write -b 123:
:rados -p mypool put objectone <somefile>:
:rados -p mypool put objecttwo <anotherfile>:
:rados -p mypool ls:

:ceph osd pool create testpool 128 128:
:rados bench 60 write -p testpool:  # rm -rf out dev

:test infrastructure:
    `<https://pulpito.ceph.com/>`_

