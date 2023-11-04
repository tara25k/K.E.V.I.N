live_loop :foo do
  use_real_time
  a, b, c = sync "/osc*/trigger/prophet"
  synth :prophet, note: a, cutoff: b, sustain: c
end

#server code to play a synth note
use_synth :prophet
live_loop :foo do
  use_real_time
  a = sync "/osc*/trigger/prophet"
  play a
 end