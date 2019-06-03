# Calculate Investments Performance
1. Run servece:
```sh
docker-compose up
```
2. UI default available on 8080 port. Port configured on .env file
http://localhost:8080/

## Using API
1. Get available URLs
```sh
curl http://localhost:8080/api/
```
2. Calculate performance for investments in BTC and ETH started in one day
```sh
curl http://localhost:8080/api/v1/performance/2017/9/1/1000/
```
this method return profitability separated on months with total profitability in every month for investments by 1000 USD started 2017-09-1 
