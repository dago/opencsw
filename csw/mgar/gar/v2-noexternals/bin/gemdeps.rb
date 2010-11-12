#!/opt/csw/bin/ruby
require 'yaml'
require 'rubygems'
spec = YAML::load(STDIN)
spec.dependencies.each do |dep|
  printf "%s\n", dep.name if dep.type == :runtime
end
