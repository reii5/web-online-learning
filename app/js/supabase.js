import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm';

const supabaseUrl = 'https://pcmxomsxjouhskyevclf.supabase.co';
const supabaseKey = 'sb_publishable_i6rwlJr6bQncqCIHxb-hJQ_yv4axrMu';

export const supabase = createClient(supabaseUrl, supabaseKey);
