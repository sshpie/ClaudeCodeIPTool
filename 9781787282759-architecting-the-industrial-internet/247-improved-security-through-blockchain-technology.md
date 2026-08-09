# Improved security through blockchain technology

Blockchain technology provides a means of building a secure, shared, and distributed database that can't be modified, often referred to as a distributed ledger, ensuring that data remains in its original, unaltered state. Data is replicated across many nodes. New transactions are digitally signed for security, with private keys used to create signatures and public keys used to verify the signatures. When participating nodes agree the data is valid, it is written to the database. The unique digital signatures ensure no individual blockchain node can modify the transaction message.

Transactions contain information about the sender, receiver, time of creation, data to be transferred, and reference transactions. Transactions are grouped together in blocks and a chain is created that maintains a history of ownership of digital assets from previous transactions. Blocks are added to the blockchain when validity of transactions is assured through *consensus.* Each block includes a hash of the prior block.

Blockchains are implemented across geographically separated distributed systems and storage and attain better parallelism, reliability, and availability in such configurations. Consensus is achieved through weak consistency models, a practical approach when many nodes are used to determine validity.

Blockchains first came into being as the underlying architecture for Bitcoin. In November 2008, a paper was published by an author using the name of Satoshi Nakamoto (never validated as a real person) and entitled *Bitcoin: A Peer-to-Peer Electronic Cash System*. The first bitcoins were issued in January 2009. By 2014, **blockchain 2.0** had emerged, describing new applications that could be built on the distributed blockchain database.

Blockchains were being investigated for usefulness in several IIoT applications at the time this book was published in 2017. Possible use cases being explored included the application of blockchains to improve security in the IIoT infrastructure by doing the following:

- Maintaining tamper-proof logs of transactions
- Securing device directories and broadcasts of updates
- Ensuring that items in transit are genuine and unaltered when managing supply chains
- Ensuring secure control of electrical grids and the delivery of power only to validated endpoints

Blockchains and other, less sophisticated security mechanisms are believed to be under threat in the future from powerful quantum computers. However, there are already efforts underway to create quantum key distributions for use with blockchains to secure them when quantum computers become practical for use in attacking today's cryptographic solutions.
