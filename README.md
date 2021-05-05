# moneymoney-datev-kassenbuch
A Python script that converts a MoneyMoney export to the DATEV Kassenbuch CSV format

I am using [MoneyMoney](https://moneymoney-app.com/) for my (business) online banking.
One of the monthly bookkeeping tasks is to export the account statement for my business
credit card and import them into DATEV (which, unlike the checking account, can't automatically
import these from my bank). Unfortunately, the MoneyMoney CSV format does not match DATEV's,
so I wrote a Python script that reads a MoneyMoney export and converts it into DATEV Kassenbuch
compatible csv files (one for each month).