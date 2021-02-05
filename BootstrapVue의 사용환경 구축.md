# BootstrapVue의 사용환경 구축

1. Vue.js 설치
2. npm 을 이용해서 BootstrapVue 설치

```bash
npm install vue bootstrap-vue bootstrap

```

3. main.js에 BootstrapVue 등록

```bash
# main.js

import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
```

4. Bootstrap과 BootstrapVue의 css를 추가합니다.

```bash
# main.js
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

```



**지금까지의 작업을 통해 BootsrapVue를 사용할 수 있다.**









