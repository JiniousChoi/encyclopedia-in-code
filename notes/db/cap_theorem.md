# CAP theorem
- implies that in the presence of a network partition, one has to choose between consistency and availability.
- CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.

## Consistency
- Every read receives the most recent write *or* an error
- it's quite different from the consistency guaranteed in ACID database transactions.

## Availability
- Every request receives a (non-error) response – without the guarantee that it contains the most recent write.

## Partition tolerance
- The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes. 

### Examples
- MySQL is CA
- CouchDB is AP
- MongoDB is CP
