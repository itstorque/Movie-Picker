source "https://rubygems.org"

gem "minima", "~> 2.5"

gem "github-pages", 202#group: :jekyll_plugins

group :jekyll_plugins do
  # gem "jekyll-feed"#, "~> 0.12"
  gem 'jekyll-remote-theme'
  #gem "jekyll-theme-console"
end

install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?
