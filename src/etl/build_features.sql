DROP TABLE IF EXISTS modeling_churn;

CREATE TABLE modeling_churn AS
    SELECT 
        customerID,

        CASE WHEN Churn = 'YES' THEN 1 ELSE 0 END AS churn_flag,


        tenure,
        MonthlyCharges,
        TotalCharges,

        ROUND(TotalCharges * 1.0 / NULLIF(tenure,0),2) AS avg_monthly_charge,


        CASE
            WHEN tenure BETWEEN 0 AND 12 THEN '0-12'
            WHEN tenure BETWEEN 13 AND 24 THEN '13-24'
            WHEN tenure BETWEEN 25 and 48 THEN '25-48'
            ELSE '49-72'

        END AS tenure_bucket, 



        CASE WHEN OnlineSecurity = 'No internet service' THEN 'No' ELSE OnlineSecurity END AS OnlineSecurity
        CASE WHEN OnlineBackup = 'No internet service' THEN 'No' ELSE OnlineBackup END AS OnlineBackup
        CASE WHEN DeviceProtection = 'No internet service' THEN 'No' ELSE DeviceProtection END AS DeviceProtection 
        CASE WHEN TechSupport = 'No internet service' THEN 'No' ELSE TechSupport END AS TechSupport
        CASE WHEN StreamingTV = 'No internet service' THEN 'No' ELSE StreamingTV END AS StreamingTV
        CASE WHEN StreamingMovies = 'No internet service' THEN 'No' ELSE StreamingMovies END AS StreamingMovies

        Contract,
        PaymentMethod,
        InternetService

        FROM raw_churn
        WHERE TotalCharges IS NOT NULL;