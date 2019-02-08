# Examples of using the Viptela vManage API

## get_unassigned_certificates.py
Use this program to get a list of certificates on the vManage that have not yet been assigned.  Output provided shows the certificate #, the token, and the chassis number that can be used to provision a vEdge

Example:

```
$> python3 ./get_unassigned_certificates.py
Please enter vManage IP address: 34.212.149.14
Please enter a vManage username: BobBarker
Please enter the password for BobBarker:
 #: Token                               Chassis #
 0: cc61144047218525b47010368712cee5    6f9267fc-603b-4b50-b97f-8285864bce41
 2: b3011f48862716ec895e101634159cb4    b8c7c191-7874-40ce-8411-8c11366f189b
 6: 3e4e5118113e40c789c6b7c16eccb1f4    9eb43f4e-4701-4318-beb8-b05f7e9cb41e
 8: 38f3be7813192bbf1b098fe682c65023    7eef7b9c-ff77-493f-b825-ee5960fb18c1
 9: 1b70ff4c824cf7c4199341919fc648fe    ec464e89-8e59-4424-8f8c-e8417714177f
10: 98e63526c9212c871b141f08c7251599    1f14517c-b3b3-4361-8c46-388913e12998
12: 3eb18b18c1e187386c58444529f92351    88531017-8f11-44f1-8e1e-78544e461743
15: 0e2fb2727388109205779490735f3071    8b1bf1b6-079b-4e8f-8f86-56f0922b8272
17: b8bf80168b7089ef54c74f511f2f2849    3e964f23-e588-449e-89c7-3f29c81111c6
21: 821b3c55c5174421940b7bf1f1451153    1ce86854-70c1-4f23-9718-38c8211ec2e8
22: 178c4f165c96e83f917015438841e967    9b59fb07-82b6-481b-8c73-11774bee4fbe
```
