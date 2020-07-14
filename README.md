# remote-work
seleniumを使ってリモートワークの開始&離席登録を自動化

## 手順
https://masakimisawa.com/selenium_headless-chrome_python_on_lambda/

## バージョン
https://www.tolog.site/aws/selenium-in-lambda/

## 構成
- cloudwatch
  - 定時トリガー
- lambda
  - serverless chrome の立ち上げ
  - サイトの自動操作　https://jisou.it-builder.jp/app/zaseki/jisou_input
- lambda layer
  - selenium
  - chromedriver
  - serverless chrome