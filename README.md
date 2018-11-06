# Examples of using the Viptela vManage API

## get_unassigned_certificates.py
Use this program to get a list of certificates on the vManage that have not yet been assigned.  Output provided shows the certificate #, the token, and the chassis number that can be used to provision a vEdge

Example:
`$ python3 ./get_unassigned_certificates.py '34.23.19.126' 'admin' 'password'
11 1b70ff4c824cf7c4d9934d919fc648fe ec464ea9-ae59-4424-8fac-ea4d7714177f
12 cc6dd44047218525b4701036a712cee5 6f9267fc-603b-4b50-b97f-a2a5a64bce41
13 0e2fb27273a8109205779490735f307d ab1bf1b6-079b-4eaf-afa6-56f0922ba272
14 3e4e51d8dd3e40c7a9c6b7c16eccb1f4 9eb43f4e-4701-43d8-beb8-b05f7e9cb41e
15 a2db3c55c5174421940b7bf1fd451d53 dcea6854-70cd-4f23-97da-38ca211ec2e8
16 9ae63526c92d2c871b141f08c725d599 1f145d7c-b3b3-4361-8c46-388913e1299a
17 b3011f488627d6ec895e10d634159cb4 b8c7c19d-7874-40ce-a4dd-ac11366f189b
18 b8bf8016ab70a9ef54c74f5d1f2f2849 3e964f23-e5aa-449e-a9c7-3f29caddd1c6
19 38f3be7a13192bbfdb098fe6a2c65023 7eef7b9c-ff77-493f-ba25-ee5960fbd8cd
20 17ac4fd65c96e83f9170d5438a4de967 9b59fb07-a2b6-4a1b-ac73-d1774bee4fbe
21 3ebdabdac1e1a7386c58444529f92351 8a53d0d7-afdd-44fd-aede-78544e461743
$`


