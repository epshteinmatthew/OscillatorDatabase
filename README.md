# Oscillator Database
## A Web-Based Database for Chemical Network Models

A database hosted on the internet can be a cost-effective and user-friendly method of publishing and accessing chemical network models. In this project, we use GitHub repositories to store the aforementioned models. We also implement several interfaces through which users can access the models, as well as a workflow for contributors to add to the database itself. We conclude that, at a reasonable scale, this implementation achieves the goals of cost-effectiveness and user-friendliness, and is thus fit for further use. We find that the database is able to perform in a satisfactory manner and without significant slowdowns at scale.

### Important Links:

- Website: https://sys-bio.github.io/cesium/
- Package on PyPi: https://pypi.org/project/oscillatorlookups/
- Preprint: 


### Testing the Web Client

In lieu of an automated test suite for the web-based database client, one can test the functionality of said client by following the steps that follow:
1. Navigate to https://sys-bio.github.io/cesium/ on a web browser
2. Select the "oscillator" option from the drop-down "model type" menu
3. Verify that the number of models found is 2065
4. Click the "download found models" button and wait for the ZIP archive to download
5. Extract the ZIP archive and verify that the extracted folder contains 2065 items
6. Using the "Number of Species" slider, set an upper limit of 2 species
7. Verify that the number of models found is 1
8. Click the "download found models" button and wait for the ZIP archive to download
9. Extract the ZIP archive and verify that the downloaded file contains the following:
   
    ```
    var S0
    var S1
    ext S2
    S1 -> S1+S1; k0*S1
    S1 + S0 -> S0 + S0; k1*S1*S0
    S2 + S0 -> S2; k2*S2*S0
    k0 = 53.47769790578378
    k1 = 21.620804940483517
    k2 = 34.2677349481839
    S0 = 1.0
    S1 = 5.0
    S2 = 9.0
    ```
