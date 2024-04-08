Sub ExtractAndSaveEmbeddedFiles()
    Dim objEmbeddedShape As InlineShape
    Dim strShapeType As String
    Dim strEmbeddedDocName As String
    Dim objEmbeddedDoc As Object
    Dim objId As Integer
    objId = 1

    Dim filename As String
    filename = ActiveDocument.Name

    Dim directory As String
    directory = "C:\Users\Georg\OneDrive\Documents\Personal\Notes\Markdown\Media\" & Left(filename, InStrRev(filename, ".") - 1) & "\"
    
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
                strEmbeddedDocName = objEmbeddedShape.OLEFormat.IconName
                objEmbeddedDoc.SaveAs directory & objId
                objEmbeddedDoc.Close
                
                Set objEmbeddedDoc = Nothing
            End If
            objId = objId + 1
        Next objEmbeddedShape
    End With
End Sub

