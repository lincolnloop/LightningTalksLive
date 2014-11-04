'use strict';
var gulp = require('gulp');
var gutil = require('gulp-util');
// sass
var sass = require('gulp-sass');
// sourcemaps
var sourcemaps = require('gulp-sourcemaps');
// livereload
var livereload = require('gulp-livereload');
// js
var watchify = require('watchify');
var browserify = require('browserify');
var source = require('vinyl-source-stream');

// --------------------------
// SASS (dev)
// --------------------------
gulp.task('sass', function() {
  return gulp.src('./client/scss/*.scss')
    .pipe(sourcemaps.init())
    .pipe(sass())
    // error logging
    .on('error', gutil.log)
    // write sourcemaps to a specific directory
    .pipe(sourcemaps.write('./'))
    // give it a file and save
    .pipe(gulp.dest('./static/css'));
});

// --------------------------
// Browserify (dev)
// --------------------------
gulp.task('browserify', function() {
  var bundler = watchify(browserify('./client/js/index.js', watchify.args));
  var rebundle = function() {
    return bundler.bundle()
      .on('error', gutil.log.bind(gutil, 'Browserify Error'))
      .pipe(source('ltl.js'))
      .pipe(gulp.dest('./static/js/')).pipe(livereload());
  }
  bundler.on('update', rebundle);

  return rebundle();
});


// --------------------------
// DEV/WATCH TASK
// --------------------------
gulp.task('watch', ['sass', 'browserify'], function() {
  livereload.listen(35729, function(err){
    gutil.log(gutil.colors.bgGreen('... Listening on 35729...'));
    if (err) {
      return console.log(err);
    }
  });

  gulp.watch('./static/css/**/*.css').on('change', function(event) {
    gutil.log(gutil.colors.bgBlue('Reloading css...'));
    livereload.changed(event.path);
  });

  // watch the sources and rebuild
  gulp.watch('./client/scss/**/*.scss', ['sass']);

  gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});

// build task
gulp.task('build', [
  'sass'
]);

gulp.task('default', ['watch']);
