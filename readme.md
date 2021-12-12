# テーブル仕様

故障や問い合わせ、依頼など運用業務に関する情報を一元的に管理するためのシステム（たたき台）

個人の好みで作成しているので汎用的ではないです。

## メインテーブル
テーブル名: *incidents_info*

すべての情報を一元的に登録するテーブル

| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|システムID|
|system_id|foreign key(system_info)|システム関連キー|
|category_id|foreign key(category_info)|カテゴリ関連キー|
|incident_id|char(300)|インシデントID|
|status_id|foreign key(status_info)|ステータス|
|subject|char(10000)|件名|
|detail|text|内容|
|timeline|text|対応内容|
|escalate|boolean|エスカレーション有無|
|create_date|datetime auto input on create|起票日|
last_modified|datedatetime auto update on update|更新日|
|publish_start|datetime| 公開開始日|
|publish_end|datetime|公開終了日|

## 付属テーブル
メインテーブルに紐付ける情報を登録するテーブル
基本的に
メイン１：付属1
の組み合わせとなる。
添付ファイルについては
メイン1：付属N
の組み合わせとなるため、付属側にincident_idを参照させている

###  ステータス情報
テーブル名; *statuses_info*

| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|ステータスID|
|status_name|char(300), not null|ステータス名|
|status_enable|boolean, not null default=true|有効/無効フラグ|
|create_date|date|登録日|
|modified_date|date|更新日|
|memo|text|備考|


### システム情報
テーブル名; *systems_info*

| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|システムID|
|system_name|char(300), not null|システム名|
|system_enable|boolean, not null default=true|有効/無効フラグ|
|system_code|char(300)| システムコード|
|create_date|date|登録日|
|memo|text|備考|

### カテゴリ
テーブル名; *categories_info*

| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|カテゴリID|
|category_name|char(300), not null|カテゴリ名|
|category_enable|boolean, not null default=true|有効/無効フラグ|
|create_date|date|登録日|
|memo|text|備考|

### 添付ファイル
テーブル名; *attachments_info*


| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|添付ファイルID|
|incident_id|foreign key(incidnet_info|関連するインシデントID|
||attachment_name|char(10000), not null|添付ファイル名|
||attachment_body|binary|添付ファイル本体|
|create_date|date|登録日|
|memo|text|備考|

### エスカレーション情報
テーブル名; *escalates_info*

| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|エスカレーションID|
|incident_id|foreign key(incidnet_info|関連するインシデントID|
|escalate_time |date, not null|エスカレーション時間|
|escalate_delay_flg |boolean, not null|遅延フラグ|
|create_date|char(100)|遅延理由番号|
|memo|text|遅延理由詳細|
|create_date|date|登録日時|

### テンプレート情報
テーブル名; *templates_info*

| フィールド名 | フィールド定義 | フィールド情報 |
|:---|:---|:---|
|id|auto increment, primary key|テンプレートID|
|template_name|char(1000)|テンプレート名|
|subject|char(10000)|件名のテンプレート|
|detail|text|内容のテンプレート|
|timeline|text|対応内容のテンプレート|
|escalate|boolean|エスカレーション有無のテンプレート|
|create_date|char(100)|遅延理由番号|
|memo|text|遅延理由詳細|
|create_date|date|登録日時|

