CREATE TABLE IF NOT EXISTS raw_churn (

  customerID TEXT PRIMARY KEY,
  gender TEXT,
  SeniorCitizen INTEGER,
  Partner TEXT,
  tenure INTEGER,
  PhoneService TEXT,
  MultipleLines TEXT,
  InternetService TEXT,
  OnlineSecurity TEXT,
  OnlineBackup TEXT,
  DeviceProtection TEXT,
  TechSupport TEXT,
  StreamingTV TEXT,
  Contract TEXT,
  PaperlessBilling TEXT,
  PaymentMethod TEXT,
  MonthlyCharges REAL,
  TotalCharges REAL,
  Churn TEXT 
  
);
