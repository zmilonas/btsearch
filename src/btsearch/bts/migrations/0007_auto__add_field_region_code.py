# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Region.code'
        db.add_column('bts_region', 'code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Region.code'
        db.delete_column('bts_region', 'code')


    models = {
        'bts.basestation': {
            'Meta': {'object_name': 'BaseStation'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'edit_status': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'enbi': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cdma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_common_bcch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_gsm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_lte': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_networks': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_umts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_stations'", 'to': "orm['bts.Location']"}),
            'location_details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_stations'", 'to': "orm['bts.Network']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'rnc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'station_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '16', 'blank': 'True'}),
            'station_status': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'bts.basestationpermission': {
            'Meta': {'unique_together': "(['base_station', 'permission', 'station_id'],)", 'object_name': 'BaseStationPermission'},
            'base_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': "orm['bts.BaseStation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_stations'", 'to': "orm['uke.Permission']"}),
            'station_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'})
        },
        'bts.cell': {
            'Meta': {'object_name': 'Cell'},
            'azimuth': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'base_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cells'", 'to': "orm['bts.BaseStation']"}),
            'cid': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cid_long': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ping': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'ecid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lac': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'ua_freq': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'bts.location': {
            'Meta': {'ordering': "['town']", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'location_hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': "orm['bts.Region']"}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'bts.network': {
            'Meta': {'ordering': "['code']", 'object_name': 'Network'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'operator_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'bts.region': {
            'Meta': {'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'uke.location': {
            'Meta': {'ordering': "['id']", 'object_name': 'Location'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'latitude_uke': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'location_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'longitude_uke': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'uke.operator': {
            'Meta': {'object_name': 'Operator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uke_operators'", 'to': "orm['bts.Network']"}),
            'operator_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'uke.permission': {
            'Meta': {'object_name': 'Permission'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'case_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'}),
            'case_number_orig': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'case_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': "orm['uke.Location']"}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'null': 'True', 'to': "orm['bts.Network']"}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': "orm['uke.Operator']"}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'station_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bts']