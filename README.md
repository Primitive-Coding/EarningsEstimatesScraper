# EarningsEstimates

- Get historical EPS, and predicted EPS by analysts via the Alpha Vantage Api.

---

### Setup

1. Setup your `config.json` file.

```
    {
      "chrome_driver_path": "D:\\PATH TO CHROME DRIVER\\chromedriver.exe",
      "data_export_path": "D:\\PATH TO EXPORT DATA"
    }
```

2. Install requirements for the project.

```
   pip install -r requirements.txt
```

3. Get a free api key from `https://www.alphavantage.co/` and configure the ".env" file.

```
    alpha_vantage_key = "API KEY HERE"
```

### Output Example:

- fiscalDateEnding: End of the fiscal period.
- reportedDate: Date the earnings report was released.
- reportedEPS: The Earnings-Per-Share (EPS) reported for the fiscal period.
- estimateEPS: The Earnings-Per-Share (EPS) estimated by analysts.
- surprise: Nominal difference from the `reportedEPS` and the `estimatedEPS`. `surprise = reportedEPS - estimatedEPS`
- surprisePercentage: Percentage difference between `reportedEPS` and `estimatedEPS`. `surprisePercentage = (surprise / estimatedEPS) \* 100`

```
                  reportedDate  reportedEPS  estimatedEPS  surprise  surprisePercentage   reportTime
fiscalDateEnding
2024-03-31         2024-05-02       1.5300          1.50    0.0300              2.0000  post-market
2023-12-31         2024-02-01       2.1800          2.10    0.0800              3.8095  post-market
2023-09-30         2023-11-02       1.4600          1.39    0.0700              5.0360  post-market
2023-06-30         2023-08-03       1.2600          1.19    0.0700              5.8824  post-market
2023-03-31         2023-05-04       1.5200          1.43    0.0900              6.2937  post-market
...                       ...          ...           ...       ...                 ...          ...
1997-03-31         1997-04-16      -0.0500         -0.04   -0.0100            -25.0000   pre-market
1996-12-31         1997-01-15      -0.0300         -0.02   -0.0100            -50.0000   pre-market
1996-09-30         1996-10-16       0.0018         -0.01    0.0118            118.0000   pre-market
1996-06-30         1996-07-17      -0.0200         -0.04    0.0200             50.0000   pre-market
1996-03-31         1996-04-17      -0.0700         -0.05   -0.0200            -40.0000   pre-market
```
