import Vue from 'vue'
import colors from 'vuetify/es5/util/colors'
import Vuetify, {VSnackbar, VIcon} from 'vuetify/lib'
import VuetifyToast from 'vuetify-toast-snackbar'

Vue.use(Vuetify, {
  components: {
    VSnackbar,
    VIcon
  },
  theme: {
    primary: colors.indigo.darken4,
    accent: colors.grey.darken3,
    secondary: colors.amber.darken3,
    info: colors.teal.lighten1,
    warning: colors.amber.base,
    error: colors.deepOrange.accent4,
    success: colors.green.accent3
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
