from rest_framework.response import Response

from storage.models import StorageDoc, StorageDocTable, Remains


def doc_close(doc_id):
    try:
        doc = StorageDoc.objects.get(id=doc_id)
        doc_list = StorageDocTable.objects.filter(storage_doc=doc_id)
        if doc.status == 'open':
            for obj in doc_list:
                try:
                    if Remains.objects.filter(goods=obj.goods,  storage=obj.storage_doc.storage).exists():
                       rem_obj = Remains.objects.filter(goods=obj.goods, storage=obj.storage_doc.storage).first()
                       rem_obj.qnt = rem_obj.qnt + obj.goods_qnt
                       rem_obj.save()
                    else:
                        Remains.objects.create(
                            goods=obj.goods,
                            qnt=obj.goods_qnt,
                            storage=doc.storage,
                        )
                except:
                    return Response({'status': f'Storage Doc №{doc.id} can not be closed'}, status=200)
            doc.status = 'close'
            doc.save()
            return Response({'status': f'Storage Doc №{doc.id} CLOSED'}, status=200)
        return Response({'status': f'Already closed doc_id: {doc_id}'}, status=400)
    except:
        return Response({'status': f'Incorrect data, doc_id: {doc_id}'}, status=400)


def doc_open(doc_id):
    try:
        doc = StorageDoc.objects.get(id=doc_id)
        doc_list = StorageDocTable.objects.filter(storage_doc=doc_id)
        if doc.status == 'close':
            for obj in doc_list:
                try:
                    if Remains.objects.filter(goods=obj.goods,  storage=obj.storage_doc.storage).exists():
                       rem_obj = Remains.objects.filter(goods=obj.goods, storage=obj.storage_doc.storage).first()
                       rem_obj.qnt = rem_obj.qnt - obj.goods_qnt
                       if rem_obj.qnt < 0:
                           rem_obj.qnt = 0
                       rem_obj.save()
                except:
                    return Response({'status': f'Storage Doc №{doc.id} can not be opened'}, status=200)
            doc.status = 'open'
            doc.save()
            return Response({'status': f'Storage Doc №{doc.id} OPENED'}, status=200)
        return Response({'status': f'Already open doc_id: {doc_id}'}, status=400)
    except:
        return Response({'status': f'Incorrect data, doc_id: {doc_id}'}, status=400)


