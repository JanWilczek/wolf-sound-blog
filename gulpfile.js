// Load plugins
const gulp = require("gulp");

// Copy third party libraries from /node_modules into /vendor
gulp.task('vendor', function(cb) {

  // Do not update Start Bootstrap Clean Blog, because the library files were manually altered.
  // Start Bootstrap Clean Blog SCSS
  //   gulp.src([
  //       './node_modules/startbootstrap-clean-blog/scss/**/*'
  //     ])
  //     .pipe(gulp.dest('./assets/vendor/startbootstrap-clean-blog/scss'))

  // Start Bootstrap Clean Blog JS
  //   gulp.src([
  //       './node_modules/startbootstrap-clean-blog/js/clean-blog.min.js',
  //       './node_modules/startbootstrap-clean-blog/js/jqBootstrapValidation.js'
  //     ])
  //     .pipe(gulp.dest('./assets/vendor/startbootstrap-clean-blog/js'))

  // Bootstrap
  gulp.src([
      './node_modules/bootstrap/dist/**/*',
      '!./node_modules/bootstrap/dist/css/bootstrap-grid*',
      '!./node_modules/bootstrap/dist/css/bootstrap-reboot*'
    ])
    .pipe(gulp.dest('./assets/vendor/bootstrap'))

  // jQuery
  gulp.src([
      './node_modules/jquery/dist/*',
      '!./node_modules/jquery/dist/core.js'
    ])
    .pipe(gulp.dest('./assets/vendor/jquery'))

  // Font Awesome
  gulp.src([
      './node_modules/@fortawesome/**/*',
    ])
    .pipe(gulp.dest('./assets/vendor'))

  // Trackswitch
  gulp.src([
      './node_modules/trackswitch/dist/**/*',
  ])
  .pipe(gulp.dest('./assets/vendor/trackswitch'))

  // Lazyload
  gulp.src([
    './node_modules/lazyload/lazyload.min.js',
    './node_modules/lazyload/lazyload.js'
  ])
  .pipe(gulp.dest('./assets/vendor/lazyload'))

  cb();

});

gulp.task("default", gulp.parallel('vendor'));
