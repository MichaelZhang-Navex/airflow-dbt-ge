SELECT
    vendorid AS vendor_id,
    DATEDIFF(
        SECOND,
        tpep_pickup_datetime,
        tpep_dropoff_datetime
    ) AS drive_time
FROM
    {{ ref("yellow_cab_raw") }}
