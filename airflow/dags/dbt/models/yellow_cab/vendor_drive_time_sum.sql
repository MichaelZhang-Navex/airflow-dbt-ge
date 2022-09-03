SELECT
    vendor_id,
    COUNT(vendor_id) AS trip_count,
    SUM(drive_time) AS drive_seconds,
    SUM(drive_time) / 3600 AS drive_hours
FROM
    {{ ref("vendor_drive_time") }}
GROUP BY
    vendor_id
