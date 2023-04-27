/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with source_data as (
 
   select {{ cents_to_dollars('spend') }} spend, current_date() from FIVETRAN_DB.GOOGLE_SHEETS.AFFILIATE_CACTUS

)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/
