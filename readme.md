# �e�[�u���d�l

�̏��₢���킹�A�˗��Ȃǉ^�p�Ɩ��Ɋւ�������ꌳ�I�ɊǗ����邽�߂̃V�X�e���i��������j

�l�̍D�݂ō쐬���Ă���̂Ŕėp�I�ł͂Ȃ��ł��B

## ���C���e�[�u��
�e�[�u����: *incidents_info*

���ׂĂ̏����ꌳ�I�ɓo�^����e�[�u��

| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�V�X�e��ID|
|system_id|foreign key(system_info)|�V�X�e���֘A�L�[|
|category_id|foreign key(category_info)|�J�e�S���֘A�L�[|
|incident_id|char(300)|�C���V�f���gID|
|status_id|foreign key(status_info)|�X�e�[�^�X|
|subject|char(10000)|����|
|detail|text|���e|
|timeline|text|�Ή����e|
|escalate|boolean|�G�X�J���[�V�����L��|
|create_date|datetime auto input on create|�N�[��|
last_modified|datedatetime auto update on update|�X�V��|
|publish_start|datetime| ���J�J�n��|
|publish_end|datetime|���J�I����|

## �t���e�[�u��
���C���e�[�u���ɕR�t�������o�^����e�[�u��
��{�I��
���C���P�F�t��1
�̑g�ݍ��킹�ƂȂ�B
�Y�t�t�@�C���ɂ��Ă�
���C��1�F�t��N
�̑g�ݍ��킹�ƂȂ邽�߁A�t������incident_id���Q�Ƃ����Ă���

###  �X�e�[�^�X���
�e�[�u����; *statuses_info*

| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�X�e�[�^�XID|
|status_name|char(300), not null|�X�e�[�^�X��|
|status_enable|boolean, not null default=true|�L��/�����t���O|
|create_date|date|�o�^��|
|modified_date|date|�X�V��|
|memo|text|���l|


### �V�X�e�����
�e�[�u����; *systems_info*

| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�V�X�e��ID|
|system_name|char(300), not null|�V�X�e����|
|system_enable|boolean, not null default=true|�L��/�����t���O|
|system_code|char(300)| �V�X�e���R�[�h|
|create_date|date|�o�^��|
|memo|text|���l|

### �J�e�S��
�e�[�u����; *categories_info*

| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�J�e�S��ID|
|category_name|char(300), not null|�J�e�S����|
|category_enable|boolean, not null default=true|�L��/�����t���O|
|create_date|date|�o�^��|
|memo|text|���l|

### �Y�t�t�@�C��
�e�[�u����; *attachments_info*


| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�Y�t�t�@�C��ID|
|incident_id|foreign key(incidnet_info|�֘A����C���V�f���gID|
||attachment_name|char(10000), not null|�Y�t�t�@�C����|
||attachment_body|binary|�Y�t�t�@�C���{��|
|create_date|date|�o�^��|
|memo|text|���l|

### �G�X�J���[�V�������
�e�[�u����; *escalates_info*

| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�G�X�J���[�V����ID|
|incident_id|foreign key(incidnet_info|�֘A����C���V�f���gID|
|escalate_time |date, not null|�G�X�J���[�V��������|
|escalate_delay_flg |boolean, not null|�x���t���O|
|create_date|char(100)|�x�����R�ԍ�|
|memo|text|�x�����R�ڍ�|
|create_date|date|�o�^����|

### �e���v���[�g���
�e�[�u����; *templates_info*

| �t�B�[���h�� | �t�B�[���h��` | �t�B�[���h��� |
|:---|:---|:---|
|id|auto increment, primary key|�e���v���[�gID|
|template_name|char(1000)|�e���v���[�g��|
|subject|char(10000)|�����̃e���v���[�g|
|detail|text|���e�̃e���v���[�g|
|timeline|text|�Ή����e�̃e���v���[�g|
|escalate|boolean|�G�X�J���[�V�����L���̃e���v���[�g|
|create_date|char(100)|�x�����R�ԍ�|
|memo|text|�x�����R�ڍ�|
|create_date|date|�o�^����|

