# investments-api
1. Run servece:
```sh
docker-compose up
```
2. Get available URLs
```sh
curl http://localhost:8080/
```
3. Calculate performance for investments in BTC and ETH started in one day
```sh
curl http://localhost:8080/v1/performance/2017/9/1/1000/
```
this method return profitability separated on months with total profitability in every month for investments by 1000 USD started 2017-09-1 
