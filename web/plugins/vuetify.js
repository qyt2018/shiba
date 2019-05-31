import Vue from 'vue'
import colors from 'vuetify/es5/util/colors'
import zhHans from 'vuetify/lib/locale/zh-Hans'
import Vuetify, {VSnackbar, VIcon} from 'vuetify/lib'
import VuetifyToast from 'vuetify-toast-snackbar'
import VuetifyConfirm from 'vuetify-confirm'

Vue.use(Vuetify, {
  components: {
    VSnackbar,
    VIcon
  }, lang: {
    locales: {zhHans},
    current: 'zhHans'
  },
  theme: {
    primary: colors.indigo.darken4,
    accent: colors.grey.darken3,
    secondary: colors.amber.darken3,
    info: colors.blue.darken3,
    warning: colors.amber.base,
    error: colors.deepOrange.accent4,
    success: colors.green.darken1
  }
});


Vue.use(VuetifyToast, {
  x: false, // default
  y: 'top', // default
  color: 'info', // default
  icon: 'info',
  classes: [
    'body-2'
  ],
  timeout: 3000, // default
  dismissable: true, // default
  autoHeight: false, // default
  multiLine: false, // default
  vertical: false, // default
  queueable: false, // default
  shorts: {
    custom: {
      color: 'purple'
    }
  },
  property: '$toast' // default
});

Vue.use(VuetifyConfirm, {
  buttonTrueText: '确定',
  buttonFalseText: '取消'
});


export default ({app}, inject) => {
  inject('toast', Vue.prototype.$toast)
}
