Sub ExtractAndSaveEmbeddedFiles()
    Dim objEmbeddedShape As InlineShape
    Dim strShapeType As String
    Dim odtName As String
    Dim objEmbeddedDoc As Object
    Dim objId As Integer
    objId = 1

    Dim directory As String
    directory = "##out_dir##\"
    
    With ActiveDocument
        For Each objEmbeddedShape In .InlineShapes
            ' Check if the shape is an embedded OLE object (not an image).
            If objEmbeddedShape.Type = wdInlineShapeEmbeddedOLEObject Then
                ' Find and open the embedded doc.
                strShapeType = objEmbeddedShape.OLEFormat.ClassType
                objEmbeddedShape.OLEFormat.Open
                
                ' Initialization
                Set objEmbeddedDoc = objEmbeddedShape.OLEFormat.Object
                
                ' Save embedded files with names as same as those of icon label.
                odtName = directory & "code-" & objId
                objEmbeddedDoc.SaveAs odtName
                objEmbeddedDoc.Close
                
                Set objEmbeddedDoc = Nothing
            End If
            objId = objId + 1
        Next objEmbeddedShape
    End With
End Sub

