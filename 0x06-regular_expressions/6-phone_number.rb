#!/usr/bin/env ruby
puts ARGV[0].scan(/\d{10}/).join
# puts ARGV[0].scan(/^\d{3}\D{1}*\d{3}\D{1}*\d{4}$/).join
