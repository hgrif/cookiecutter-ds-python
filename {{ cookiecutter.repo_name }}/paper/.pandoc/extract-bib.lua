function Pandoc(d)
  d.meta.references = pandoc.utils.references(d)
  d.meta.bibliography = nil
  return d
end