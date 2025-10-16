ALTER TABLE events 
ADD CONSTRAINT check_pure_synthetic_is_synthetic
CHECK (type != 'PURE_SYNTHETIC' OR synthetic = true);

CREATE INDEX IF NOT EXISTS idx_events_type_synthetic 
ON events(type, synthetic) 
WHERE synthetic = true;
