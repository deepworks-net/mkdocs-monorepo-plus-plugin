# Release Notes

{%- macro release_header(release='v0.0.0',release_date='(01/01/1970)',name_space='deepworks-net/mkdocs-monorepo-plus-plugin') %}
## <a href="https://github.com/{{ name_space }}/releases/tag/{{ release }}" target="_blank" title="{{ release }} Release" alt="{{ release }} Release">**{{ release }} {{ release_date }}**</a>
{% endmacro -%}

{{ release_header('v1.0.0','(08/04/2023)') }}
- Initial release