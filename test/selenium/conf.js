exports.config = {
  framework: 'jasmine',
  seleniumAddress: 'http://localhost:8000',
  capabilities: {
    'browserName': 'chrome'
  },
  specs: [
      //'signup_user_success.js',
      //'signup_user_fail.js',
      //'login_success.js',
      'login_fail.js'
  ],
  jasmineNodeOpts: {
    showColors: true, // Use colors in the command line report.
  }
};
